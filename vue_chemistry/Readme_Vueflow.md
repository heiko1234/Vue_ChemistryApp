
Create a new Vue project.
Install the Vue Flow package.
Set up Vue Flow in your project.


# Create new vue project

npm create vue@latest
cd your-project-name


# Install the Vue Flow package

npm install @vue-flow/core


# Set up Vue Flow in your project


Open src/main.js (or src/main.ts if you are using TypeScript) and import Vue Flow:


import { createApp } from 'vue';
import App from './App.vue';
import VueFlow from '@vue-flow/core';
import '@vue-flow/core/dist/style.css';

const app = createApp(App);
app.use(VueFlow);
app.mount('#app');




Use Vue Flow in your components. For example, in src/App.vue:


<template>
  <div id="app">
    <vue-flow />
  </div>
</template>

<script>
export default {
  name: 'App',
};
</script>

<style>
/* Add any custom styles here */
</style>



# Create Vue App with Vue Flow

## Create a new Vue project

```shell
npm create vue@latest
cd your-project-name

