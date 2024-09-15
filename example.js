(async () => {
  const data = await fetch("https://misso-dev.h1rose.com/distance-sensor")
  const body = await data.text()
  console.log(body)
})()
