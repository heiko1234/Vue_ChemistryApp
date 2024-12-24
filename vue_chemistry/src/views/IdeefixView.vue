<template>
    <div class="ideefix">
        <ideefixheader @roleSelected="handleRole"></ideefixheader>
        <div class="pagecontent">
            <div class="ideacards">
                <IdeeFixCard ref="editCard"></IdeeFixCard>
                <IdeeVoteCard ref="voteCard"></IdeeVoteCard>
                <IdeeImplementCard ref="implementCard"></IdeeImplementCard>
            </div>
        </div>
    </div>
  
</template>

<script>

import ideefixheader from '@/components/IdeeFix/IdeeFixHeader.vue'
import IdeeFixCard from '@/components/IdeeFix/IdeeFixCard.vue'
import IdeeVoteCard from '@/components/IdeeFix/IdeeVoteCard.vue'
import IdeeImplementCard from '@/components/IdeeFix/IdeeImplementCard.vue'

export default {
    name: "IdeefixView",
    components: {
        ideefixheader,
        IdeeFixCard,
        IdeeVoteCard,
        IdeeImplementCard
    },
    data() {
        return {
            selectedRole: 'User',
        };
    },
    methods: {
        handleRole(role) {
            this.selectedRole=role;
            this.updateCards();
        },
        updateCards() {
            console.log('update Cards');
            if (this.selectedRole ==="Developer") {
                this.$refs.editCard.isButtonActive=true;
                this.$refs.voteCard.isButtonActive=true;
                this.$refs.implementCard.isButtonActive=true;
            }
            else if (this.selectedRole==="Admin") {
                this.$refs.editCard.isButtonActive=false;
                this.$refs.voteCard.isButtonActive=false;
                this.$refs.implementCard.isButtonActive=true;
            }
            else if (this.selectedRole==="User") {
                this.$refs.editCard.isButtonActive=true;
                this.$refs.voteCard.isButtonActive=true;
                this.$refs.implementCard.isButtonActive=false;
            }
        }
    },
    mounted() {
        this.updateCards();
    }
}
</script>

<style scoped>

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

.ideacards {
    display: flex;
    flex-wrap: wrap;
    justify-content: center;
    gap: 10px;
}



</style>