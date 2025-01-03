import './assets/main.css'

import { createApp } from 'vue'
import App from './App.vue'
import Toast, { POSITION } from 'vue-toastification'
import 'vue-toastification/dist/index.css'
import router from './router'

const app = createApp(App)

app.use(Toast, {
    position: POSITION.TOP_RIGHT
  })

app.use(router)

app.mount('#app')
