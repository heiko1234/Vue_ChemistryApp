<template>
    <div class="ideefix">
        <ideefixheader></ideefixheader>
        <h1>
        Test</h1>
    </div>
  
</template>

<script>

import ideefixheader from '@/components/IdeeFix/IdeeFixHeader.vue'

export default {
    name: "IdeefixView",
    components: {
        ideefixheader
    }


}
</script>

<style>

body {
    margin: 0;
    font-family: Arial, sans-serif;
}

.ideefix {
    display: flex;
    flex-direction: column;
    align-items: center;
    justify-content: center;
    padding: 5px;
    width: 100%;
    height: 100%;
}


</style>