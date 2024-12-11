
<!-- Homeview -->

<template>
  <div>
    <promotionheader :promotion_title_text="promotion_title_text" :promotion_subtitle_texta="promotion_subtitle_texta" :promotion_subtitle_textb="promotion_subtitle_textb" />
  </div>
</template>

<script>

import promotionheader from '@/components/HomeViewContent/promotionheader.vue'

export default {
    name:"HomeView",
    components: {
        promotionheader
    },
    data() {
        return {
            promotion_title_text: "Welcome to Artemis & Apollo",
            promotion_subtitle_texta: "Build on the Past",
            promotion_subtitle_textb: " - Look to the Future"
        }
    }

}
</script>

<style>

</style>

