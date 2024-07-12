export async function loadLayoutMiddleware(route) {
  try {
      let layout = route.meta.layout.__name
      let layoutComponent = await import(`../layouts/${layout}.vue`)
      route.meta.layoutComponent = layoutComponent.default
      // console.log(layout)
  } catch (e) {
      console.error('Error occurred in processing of layouts: ', e)
      console.log('Mounted default layout AppLayoutDefault')
      let layout = 'DefaultLayout'
      let layoutComponent = await import(`@/layouts/${layout}.vue`)
      route.meta.layoutComponent = layoutComponent.default
  }
}