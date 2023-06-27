const express=require('express')
const port=process.env.PORT||3000
const path=require('path')

const publicPath=path.join(__dirname,'../build')


const app=express()
app.use(express.static(publicPath))
app.listen(port,()=>{
    console.log(`Server started at ${port}`)
  })
