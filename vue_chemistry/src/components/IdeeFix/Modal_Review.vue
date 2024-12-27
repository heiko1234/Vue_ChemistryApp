
<!-- Modal_Review gets started in IdeeVoteCard.vue via isReviewModalVisible -->

<template>
  <div class="modalrapper" v-if="isReviewModalVisible">
    <div class="backdrop" @click.self="closeReviewModal">
      <div class="reviewmodal">
        <h1>Idea Review</h1>
        <hr />
        <h4 class="text_closer"> Use a filter</h4>
        <div class="stacked_flex">
          <div class="stacked_block">
            <h3>Name</h3>
            <input type="text" class="input_text" id="review_name" v-model="review_name" />
          </div>
          <div class="stacked_block">
            <h3>Idea Title</h3>
            <input type="text" class="input_text" id="review_ideatitle" v-model="review_ideatitle" />
          </div>
          <div class="stacked_block">
            <h3>Idea Description</h3>
            <input class="input_text" id="review_ideadescription" v-model="review_ideadescription" />
          </div>
        </div>
        <hr />
        <div class="scrollable">
          <div>
          <!-- Table output -->

            <h4>Search Results</h4>
            <table v-if="ideas.length">
              <thead>
                <tr>
                  <th>Index</th>
                  <th>Name</th>
                  <th>Title</th>
                  <th>Description</th>
                  <th>Votes</th>
                </tr>
              </thead>
              <tbody>
                <tr v-for="idea in ideas" :key="idea.idea_id">
                  <td>{{ idea[0] }}</td>  <!-- Index -->
                  <td>{{ idea[1] }}</td>  <!-- Name -->
                  <td>{{ idea[2] }}</td>  <!-- Title -->
                  <td>{{ idea[3] }}</td>  <!-- Description -->
                  <!-- Votes -->
                    <td>
                      <div class="vote_flex">
                        <div class="vote-container">
                        <!-- votes next to each other -->
                        <!-- bad votes -->
                          <span class="bad_votes">{{ idea[4] }}</span>
                          <button @click="voteIdeabad(idea[0])">
                            <img src="@/assets/votes/bad.png" alt="Bad" class="vote-icon" />
                          </button>
                        </div>
                        <div class="vote-container">
                          <!-- good votes -->
                          <span class="good_votes">{{ idea[5] }}</span>
                          <button @click="voteIdeagood(idea[0])">
                            <img src="@/assets/votes/good.png" alt="Good" class="vote-icon" />
                          </button>
                        </div>
                      </div>
                  </td>
                </tr>
              </tbody>
            </table>
            <p v-else>No results found</p>

            <!-- Table end -->

          </div>
        </div>
      </div>
    </div>
  </div>
</template>

<script>
import axios from 'axios';

export default {

  name: 'ReviewModal',
  props: {
    isReviewModalVisible: {
      type: Boolean,
      required: true
    }
  },
  data() {
    return {
      review_name: '',
      review_ideatitle: '',
      review_ideadescription: '',
      ideas: []
    }
  },
  watch: {
    review_name(newVal) {
      this.searchIdeas();
    },
    review_ideatitle(newVal) {
      this.searchIdeas();
    },
    review_ideadescription(newVal) {
      this.searchIdeas();
    }
  },

  methods: {
    closeReviewModal() {
      this.$emit('closeReviewModal');
    },
    async searchIdeas() {
      try {
        console.log('searchIdeas');
        const response = await axios.post('http://127.0.0.1:8000/api/get_active_ideas_filtered', {
            name: this.review_name,
            short_title: this.review_ideatitle,
            idea_description: this.review_ideadescription
        });
        this.ideas = response.data;
        console.log('Ideas:', response.data);
      }
      catch (error) {
        console.error('Error fetching ideas:', error);
      }
    },
    async voteIdeagood(idea_id) {
      try {
        console.log('Voting on idea good');
        console.log('Idea ID:', idea_id);
        const response = await axios.post('http://127.0.0.1:8000/api/vote_idea_good', {
          idea_id: idea_id,
        });
          console.log('Vote response:', response.data);
          this.searchIdeas(); // Refresh the ideas list after voting
        }
        catch (error) {
          console.error('Error voting on idea:', error);
      }
    },
    async voteIdeabad(idea_id) {
      try {
        console.log('Voting on idea bad');
        console.log('Idea ID:', idea_id);
        const response = await axios.post('http://127.0.0.1:8000/api/vote_idea_bad', {
          idea_id: idea_id,
        });
          console.log('Vote response:', response.data);
          this.searchIdeas(); // Refresh the ideas list after voting
        }
        catch (error) {
          console.error('Error voting on idea:', error);
      }
    }
  },
  mounted() {
    this.searchIdeas();
  }

}
</script>

<style scoped>
.backdrop {
    position: fixed;
    top: 0;
    left: 0;
    width: 100%;
    height: 100vh;
    background: rgba(0, 0, 0, 0.5);
    display: flex;
    justify-content: center;
    align-items: center;
    z-index: 10;
}

.reviewmodal {
    width: 90%;
    max-width: 50rem;
    background: white;
    border-radius: 6px;
    box-shadow: 0 2px 8px rgba(0, 0, 0, 0.26);
    z-index: 10;
    overflow: hidden;
}

.stacked_block{
  display: block;
  margin: 0;
  padding: 10px;
}

.stacked_flex {
    display: flex;
    justify-content: space-between;
    padding: 0;
    padding-bottom: 10px;
}

.stacked_flex h3 {
  margin: 5px;
  padding: 5px;
}

.text_closer {
  text-align: left;
  margin: 5px;
  padding: 5px;
}

.scrollable {
  overflow-y: auto;
  max-height: 600px;
  min-height: 400px;
}

table {
  width: 90%;
  border-collapse: collapse;
  margin-top: 20px;
  margin-right: 10px;
  margin-left: 10px;
}

th, td {
  padding: 10px;
  text-align: left;
  border-bottom: 1px solid #ddd;
}

th {
  background-color: #f2f2f2;
}

tr:hover {
  background-color: #f5f5f5;
}

.vote_flex {
  display: flex;
  justify-content: space-between;
}

.vote-container {
  display: flex;
  align-items: center;
  gap: 5px;
}

.vote-icon {
  width: 16px;
  height: 16px;
}

.good_votes {
  color: green;
}

.bad_votes {
  color: red;
}


</style>
