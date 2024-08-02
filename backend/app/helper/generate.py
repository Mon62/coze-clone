import google.generativeai as genai
from google.generativeai import GenerationConfig
import textwrap
import google.generativeai as genai
from IPython.display import display
from IPython.display import Markdown
from openai import OpenAI
import os
from dotenv import load_dotenv
load_dotenv()

google_api_key = os.environ['GOOGLE_API_KEY']   
genai.configure(api_key=google_api_key)

safety_settings = [
    {
        'category': 'HARM_CATEGORY_HARASSMENT',
        'threshold': 'BLOCK_NONE'
    },
    {
        'category': 'HARM_CATEGORY_HATE_SPEECH',
        'threshold': 'BLOCK_NONE'
    },
    {
        'category': 'HARM_CATEGORY_SEXUALLY_EXPLICIT',
        'threshold': 'BLOCK_NONE'
    },
    {
        'category': 'HARM_CATEGORY_DANGEROUS_CONTENT',
        'threshold': 'BLOCK_NONE'
    }
]

google_api_key = os.environ.get('GOOGLE_API_KEY')
openai_api_key = os.environ.get('OPENAI_API_KEY')

genai.configure(api_key=google_api_key)

def to_markdown(text):
    text = text.replace('•', '  *')
    return Markdown(textwrap.indent(text, '> ', predicate=lambda _: True))

# Gemini model  
class Gemini:
    def __init__(self, model_name, temperature, top_p, max_output_tokens) -> None:
        self.config = GenerationConfig(
            temperature=temperature,
            top_p=top_p,
            max_output_tokens=max_output_tokens
        )
        self.safety_settings = [
            {
                'category': 'HARM_CATEGORY_HARASSMENT',
                'threshold': 'BLOCK_NONE'
            },
            {
                'category': 'HARM_CATEGORY_HATE_SPEECH',
                'threshold': 'BLOCK_NONE'
            },
            {
                'category': 'HARM_CATEGORY_SEXUALLY_EXPLICIT',
                'threshold': 'BLOCK_NONE'
            },
            {
                'category': 'HARM_CATEGORY_DANGEROUS_CONTENT',
                'threshold': 'BLOCK_NONE'
            }
        ]
        self.model = genai.GenerativeModel(model_name=model_name, safety_settings=safety_settings)
    
    def invoke(self, instruction, question, chats, context):
        messages = [{'role': 'model', 'parts': [instruction]}]

        for chat in chats:
            messages.append({'role': 'user', 'parts': [chat['question']]})
            messages.append({'role': 'model', 'parts': [chat['answer']]})

        prompt = f'''
Trả lời câu hỏi sau với kiến thức của bạn và thông tin được cung cấp.
Thông tin cung cấp:{context}
Câu hỏi: {question}
'''
        messages.append({'role': 'user', 'parts': [prompt]})

        response = self.model.generate_content(messages, generation_config=self.config)

        return response.text

# GPT model
class GPT:  
    def __init__(self, model_name, temperature, top_p, frequency_penalty, presence_penalty, max_length, output_format):
        self.model_name = model_name
        self.temperature = temperature
        self.top_p = top_p
        self.frequency_penalty = frequency_penalty
        self.presence_penalty = presence_penalty
        self.max_length = max_length
        self.output_format = output_format
        self.client = OpenAI(api_key=openai_api_key)

    def invoke(self, instruction, question, chats, context):
        messages = [{'role': 'system', 'content': instruction}]

        for chat in chats:
            messages.append({'role': 'user', 'content': chat['question']})
            messages.append({'role': 'assistant', 'content': chat['answer']})

        prompt = f'''
Trả lời câu hỏi sau với kiến thức của bạn và thông tin được cung cấp.
Thông tin cung cấp:{context}
Câu hỏi: {question}
'''
        messages.append({'role': 'user', 'content': prompt})
        print(messages)

        response = self.client.chat.completions.create (
            model=self.model_name,
            frequency_penalty=self.frequency_penalty,
            presence_penalty=self.presence_penalty,
            top_p=self.top_p,
            temperature=self.temperature,
            max_tokens=self.max_length,
            messages=messages
        )
        return response.choices[0].message.content
        

# instruction = '''# Character
# Bạn là một chuyên gia marketing hiểu biết sâu rộng về các chiến lược và công cụ tiếp thị hiện đại. Bạn có khả năng phát triển và tối ưu hóa chiến dịch tiếp thị hiệu quả dựa trên yêu cầu của khách hàng.

# ## Skills
# ### Skill 1: Phân tích thị trường
# - Khám phá và phân tích xu hướng thị trường hiện tại.
# - Sử dụng googleWebSearch() để tìm kiếm thông tin và thống kê mới nhất liên quan đến dịch vụ hoặc sản phẩm của khách hàng.
# - Tóm tắt những điểm quan trọng và gợi ý chiến lược marketing dựa trên phân tích.

# ### Skill 2: Phát triển chiến dịch tiếp thị
# - Xây dựng kế hoạch tiếp thị chi tiết dựa trên yêu cầu của khách hàng.
# - Sử dụng công cụ quảng cáo trên các nền tảng như Google AdWords, Facebook, Instagram để tiếp cận đối tượng mục tiêu.
# - Đề xuất các kênh tiếp thị phù hợp và cách tối ưu hóa hiệu quả chiến dịch.

# ### Skill 3: Đo lường và tối ưu hóa
# - Sử dụng các công cụ như Google Analytics, Facebook Insights để theo dõi và đo lường hiệu quả chiến dịch.
# - Đánh giá kết quả và đề xuất cách cải thiện nếu cần thiết.
# - Báo cáo kết quả chi tiết theo yêu cầu của khách hàng.

# ## Constraints
# - Chỉ thảo luận về các chủ đề liên quan đến marketing.
# - Chỉ sử dụng những nguồn tin cậy trong việc cung cấp thông tin.
# - Sử dụng kết hợp các kiến thức nội bộ và công cụ tìm kiếm để có thông tin chính xác và cập nhật.
# '''

# knowledge = '''Tóm tắt thông số cấu hình Galaxy A55 5G:

# Màn hình: Kích thước 6.6 inch, tấm nền AMOLED, độ phân giải Full HD+ (1.080 x 2.340 pixels), tần số quét 120 Hz.
# CPU: Exynos 1480.
# RAM: 8 GB hoặc 12 GB.
# Bộ nhớ trong: 128 GB hoặc 256 GB (hỗ trợ mở rộng tối đa 1 TB qua thẻ microSD).
# Camera sau: 50 MP (chính) + 12 MP (góc siêu rộng) + 5 MP (macro).
# Camera trước: 32 MP.
# Dung lượng pin: 5.000 mAh, hỗ trợ sạc nhanh 25 W.
# Hệ điều hành: One UI 6.1 - Android 14.'''

# question = 'Hãy viết một bài marketing cho chiếc điện thoại Galaxy A55 5G.'

# # model = Gemini('gemini-1.5-flash',0.5, 0.7, 1024)

# model = GPT(model_name='gpt-3.5-turbo-0125',
#             temperature=0.7,
#             top_p=0.5,
#             frequency_penalty=0,
#             presence_penalty=0,
#             max_length=1024,
#             output_format='json_object')

# print (model.invoke(instruction, question, [], knowledge))

