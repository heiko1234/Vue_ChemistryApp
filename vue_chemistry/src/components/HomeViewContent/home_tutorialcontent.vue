<template>
  <div class="tutorial-container">
    <h1 class="tutorial-title">
    Tutorials
    </h1>

    <!-- a header for the controls, left and right with a button -->
    <div class="tutorial-controls">
        <button class="tutorial-controlbutton">
            <img
                class="tutorial-button-icon"
                src="@/assets/arrows/arrow_left.png" alt=""
                @click="handleTutorialClickleft"
            />
        </button>
        <button class="tutorial-controlbutton">
            <img
                class="tutorial-button-icon"
                src="@/assets/arrows/arrow_right.png" alt=""
                @click="handleTutorialClickright"
            />
        </button>
    </div>
    <!-- scrolable content left to write -->
    <div class="tutorial-content">
        <TutorialCard
            v-for="tutorial in tutorials"
            :key="tutorial.title"
            :tuttitle="tutorial.title"
            :tuttag="tutorial.tag"
            :tutimage="tutorial.image"
            :tutcarddescription="tutorial.description"
        />
    </div>

  </div>
</template>

<script>

import TutorialCard from '@/components/HomeViewContent/TutorialCard.vue'

export default {
    name: 'TutorialContent',
    components: {
        TutorialCard
    },
    props: ['tutorials'],
    methods: {
        handleTutorialClickleft() {
            console.log('left')
            const tutorialContent = document.querySelector('.tutorial-content')
            tutorialContent.scrollLeft -= 200 // Adjust the scroll distance as needed
        },
        handleTutorialClickright() {
            console.log('right')
            const tutorialContent = document.querySelector('.tutorial-content')
            tutorialContent.scrollLeft += 200 // Adjust the scroll distance as needed
        }
    }

}
</script>

<style scoped>

.tutorial-container {
    display: block;
    align-items: center;
    justify-content: center;
    padding: 1rem;
    background-color: transparent;
}

.tutorial-title {
    font-family: Arial, Helvetica, sans-serif;
    font-size: 2rem;
    color: #000;
    text-align: center;
    padding: 1rem;
    margin: 0.5rem;
}

.tutorial-controls {
    display: flex;
    justify-content: center;
    align-items: center;
    padding: 1rem;
}

.tutorial-controlbutton {
    display: flex;
    justify-content: center;
    align-items: center;
    padding: 1rem;
    margin: 0.5rem;
    background-color: transparent;
    color: var(--secondary-color);
    border: none;
    cursor: pointer;
}

.tutorial-button-icon {
    width: 2rem;
    height: 2rem;
    cursor: pointer;
}

.tutorial-button-icon:hover {
    background-color: var(--secondary-color);
    border-radius: 50%;
}

.tutorial-content {
    display: flex;
    justify-content: center;
    align-items: center;
    padding: 1rem;
    margin: 0.5rem;
    background-color: transparent;
    overflow-x: auto;
    flex-wrap: nowrap;
    scroll-behavior: smooth;
}


</style>