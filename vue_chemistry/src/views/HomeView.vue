
<!-- Homeview -->

<template>
  <div>
    <promotionheader :promotion_title_text="promotion_title_text" :promotion_subtitle_texta="promotion_subtitle_texta" :promotion_subtitle_textb="promotion_subtitle_textb" />
    <homeviewheader @scroll-to-section="handleScrollToSection" />
    <div class="scroll-div">
        <section id="Product">
            <!-- <h1> Product</h1> -->
            <productinfo
            :ińfo_product_title="product_title"
            :info_product_subtitle="product_subtitle"
            :info_product_shortdescription="product_shortdescription"
            :info_text="info_text"
        />
        </section>
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
import productinfo from '@/components/HomeViewContent/home_product_info.vue'

export default {
    name:"HomeView",
    components: {
        promotionheader,
        homeviewheader,
        productinfo
    },
    data() {
        return {
            promotion_title_text: "Artemis & Apollo",
            promotion_subtitle_texta: "Build on the Past",
            promotion_subtitle_textb: " - Look to the Future",
            // Productinfos
            info_product_title: "Apollo",
            info_product_subtitle: "The God of the future",
            info_product_shortdescription: "Apollo is the god of the future. He is the god of prophecy, music, healing, light, and truth. He is the son of Zeus and Leto, and the twin brother of Artemis. Apollo is the ideal of the kouros, which means he has a beardless, athletic youth. He is also the god of the sun, and is often depicted with a bow and arrow.",
            info_text: "Apollo is the god of the future. He is the god of prophecy, music, healing, light, and truth. He is the son of Zeus and Leto, and the twin brother of Artemis. Apollo is the ideal of the kouros, which means he has a beardless, athletic youth. He is also the god of the sun, and is often depicted with a bow and arrow.",
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

