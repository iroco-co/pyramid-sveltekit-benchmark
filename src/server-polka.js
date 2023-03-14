import { handler } from './build/handler.js'
import  polka from 'polka'


polka()
  .use(handler)
  .listen(3000, () => {
    console.log(`> Running on localhost:3000`)
  });
