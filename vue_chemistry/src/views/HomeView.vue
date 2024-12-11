
<!-- Homeview -->

<template>
  <div>
    <promotionheader :promotion_title_text="promotion_title_text" :promotion_subtitle_texta="promotion_subtitle_texta" :promotion_subtitle_textb="promotion_subtitle_textb" />
    <homeviewheader @scroll-to-section="handleScrollToSection" />
    <div class="scroll-div">
        <section id="About">
            <h1> About</h1>
        </section>

        <section id="Tutorials">
            <h1> Tutorials</h1>
        </section>
    </div>
  </div>
</template>

<script>

import promotionheader from '@/components/HomeViewContent/promotionheader.vue'
import homeviewheader from '@/components/HomeViewContent/homeviewheader.vue'

export default {
    name:"HomeView",
    components: {
        promotionheader,
        homeviewheader
    },
    data() {
        return {
            promotion_title_text: "Artemis & Apollo",
            promotion_subtitle_texta: "Build on the Past",
            promotion_subtitle_textb: " - Look to the Future"
        }
    },
    methods: {
        handleScrollToSection(section) {
            const element = document.getElementById(section);
            if (element) {
                element.scrollIntoView({ behavior: 'smooth' });
            }
        }
    }

}
</script>

<style>

</style>

