<template>
    <div class="ideefix">
        <ideefixheader></ideefixheader>
        <div class="pagecontent">
            <IdeeFixCard></IdeeFixCard>
        </div>
    </div>
  
</template>

<script>

import ideefixheader from '@/components/IdeeFix/IdeeFixHeader.vue'
import IdeeFixCard from '@/components/IdeeFix/IdeeFixCard.vue'

export default {
    name: "IdeefixView",
    components: {
        ideefixheader,
        IdeeFixCard
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
    overflow: hidden;
}

.ideefixheader {
    width: 100%;
    position: fixed;
    top: 0;
}

.pagecontent {
    margin-top: 60px;
    height: calc(100vh-60px);
    overflow-y: auto;
    padding: 10px;
}


</style>