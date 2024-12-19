
<!-- Homeview -->

<template>
  <div>
    <promotionheader :promotion_title_text="promotion_title_text" :promotion_subtitle_texta="promotion_subtitle_texta" :promotion_subtitle_textb="promotion_subtitle_textb" />
    <homeviewheader @scroll-to-section="handleScrollToSection" @open-contact-modal="toggleModal"/>
    <ContactModal :isContactModalVisible="isModalVisible" @closeContactModal="toggleModal">
      <h1>Contacts</h1>
      <p>My contacts</p>
    </ContactModal>
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
            <!-- <h1> About</h1> -->
            <HomeAboutInfo
            :homeinfotext1="about_text"
            :homeinfotext2="about_text2"
            :homeinfotext3="about_text3"
            />
        </section>

        <section id="Tutorials">
            <!-- <h1> Tutorials</h1> -->
            <TutorialContent
            :tutorials="tutorials"
            />
        </section>
    </div>
  </div>
</template>

<script>

import promotionheader from '@/components/HomeViewContent/promotionheader.vue'
import homeviewheader from '@/components/HomeViewContent/homeviewheader.vue'
import productinfo from '@/components/HomeViewContent/home_product_info.vue'
import ContactModal from '@/components/HomeViewContent/contactmodal.vue'
import HomeAboutInfo from '@/components/HomeViewContent/home_content_info.vue'
import TutorialContent from '@/components/HomeViewContent/home_tutorialcontent.vue'


export default {
    name:"HomeView",
    components: {
        promotionheader,
        homeviewheader,
        ContactModal,
        productinfo,
        HomeAboutInfo,
        TutorialContent
    },
    data() {
        return {
            //Modal
            isModalVisible: false,
            // Promotionheader
            promotion_title_text: "Artemis & Apollo",
            promotion_subtitle_texta: "Build on the Past",
            promotion_subtitle_textb: " - Look to the Future",
            // Productinfos
            info_product_title: "Apollo",
            info_product_subtitle: "The God of the future",
            info_product_shortdescription: "Apollo is the god of the future. He is the god of prophecy, music, healing, light, and truth. He is the son of Zeus and Leto, and the twin brother of Artemis. Apollo is the ideal of the kouros, which means he has a beardless, athletic youth. He is also the god of the sun, and is often depicted with a bow and arrow.",
            info_text: "Apollo is the god of the future. He is the god of prophecy, music, healing, light, and truth. He is the son of Zeus and Leto, and the twin brother of Artemis. Apollo is the ideal of the kouros, which means he has a beardless, athletic youth. He is also the god of the sun, and is often depicted with a bow and arrow.",
            // HomeAboutInfo
            about_text: "Apollo is the god of the future. He is the god of prophecy, music, healing, light, and truth. He is the son of Zeus and Leto, and the twin brother of Artemis. Apollo is the ideal of the kouros, which means he has a beardless, athletic youth. He is also the god of the sun, and is often depicted with a bow and arrow.",
            about_text2: "Apollo is the god of the future. He is the god of prophecy, music, healing, light, and truth. He is the son of Zeus and Leto, and the twin brother of Artemis. Apollo is the ideal of the kouros, which means he has a beardless, athletic youth. He is also the god of the sun, and is often depicted with a bow and arrow.",
            about_text3: "Apollo is the god of the future. He is the god of prophecy, music, healing, light, and truth. He is the son of Zeus and Leto, and the twin brother of Artemis. Apollo is the ideal of the kouros, which means he has a beardless, athletic youth. He is also the god of the sun, and is often depicted with a bow and arrow.",
            // Tutorials
            tutorials: [
                {
                    title: "Tutorial 1",
                    tag: "Beginner",
                    description: "This is a beginner tutorial",
                    image: "Apollo4.jpeg",
                    link: "https://www.youtube.com/watch?v=9bZkp7q19f0"
                },
                {
                    title: "Tutorial 2",
                    tag: "Intermediate",
                    description: "This is an intermediate tutorial",
                    image: "datascience.jpeg",
                    link: "https://www.youtube.com/watch?v=9bZkp7q19f0"
                },
                {
                    title: "Tutorial 3",
                    tag: "Advanced",
                    description: "This is an advanced tutorial",
                    image: "datascience.jpeg",
                    link: "https://www.youtube.com/watch?v=9bZkp7q19f0"
                }
            ],
            // Roadmap
            roadmap: [
                {
                    title: "Now",
                    list: [
                        "Landing Page",
                        "Product Page",
                        "Onboarding"
                    ]
                },
                {
                    title: "Next",
                    list: [
                        "User Authentication",
                        "User Dashboard",
                        "User Settings"
                    ]
                },
                {
                    title: "Future",
                    list: [
                        "Mobile App",
                        "Machine Learning",
                        "AI"
                    ]
                }
            ],
            // FAQ
            faq: [
                {
                    question: "What is Apollo?",
                    answer: "Apollo is the god of the future. He is the god of prophecy, music, healing, light, and truth. He is the son of Zeus and Leto, and the twin brother of Artemis. Apollo is the ideal of the kouros, which means he has a beardless, athletic youth. He is also the god of the sun, and is often depicted with a bow and arrow."
                },
                {
                    question: "Who is Apollo?",
                    answer: "Apollo is the god of the future. He is the god of prophecy, music, healing, light, and truth. He is the son of Zeus and Leto, and the twin brother of Artemis. Apollo is the ideal of the kouros, which means he has a beardless, athletic youth. He is also the god of the sun, and is often depicted with a bow and arrow."
                },
                {
                    question: "Where is Apollo?",
                    answer: "Apollo is the god of the future. He is the god of prophecy, music, healing, light, and truth. He is the son of Zeus and Leto, and the twin brother of Artemis. Apollo is the ideal of the kouros, which means he has a beardless, athletic youth. He is also the god of the sun, and is often depicted with a bow and arrow."
                }
            ]
        }
    },
    methods: {
        handleScrollToSection(section) {
            const element = document.getElementById(section);
            if (element) {
                element.scrollIntoView({ behavior: 'smooth' });
            }
        },
        toggleModal() {
            this.isModalVisible = !this.isModalVisible
        }
    }

}
</script>

<style scoped>

.scroll-div {
    overflow-y: auto;
    height: calc(100vh-200px);
    scroll-behavior: smooth;
}

</style>

