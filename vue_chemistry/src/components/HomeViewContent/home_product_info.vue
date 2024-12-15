<template>
  <div class="HomeProductInfo">
    <h1 class="ProductInfo-title">{{ ińfo_product_title }}</h1>
    <div class="HomeProductInfoContent">
      <div class="ProductInfo-text">
        <div class="ProductInfo_subtitle">
          {{ info_product_subtitle }}
        </div>
        <div class="HomeInfoShortdescription">
          {{ info_product_shortdescription }}
        </div>
        <p>
          {{ info_text }}
        </p>
        <div>
          <button class="Home_button_video" @click="goToVideo">
            <img class="Home_button_icon" src="@/assets/buttons_icons/arrow.png" alt="" />
            Video
          </button>
          <button class="Home_button_start" @click="$router.push('/services')">
            <img class="Home_button_icon" src="@/assets/buttons_icons/rocket2.png" alt="" />
            Get Started
          </button>
        </div>
      </div>
      <div class="HomeInfo-graphic">
        <img src="@/assets/theme/Apollo.jpeg" alt="About Graphic" style="width: 20%; height: auto" />
      </div>
    </div>
  </div>
</template>

<script>
export default {
  name: 'productinfo',
  props: {
    ińfo_product_title: {
      type: String,
      required: true
    },
    info_product_subtitle: {
      type: String,
      required: true
    },
    info_product_shortdescription: {
      type: String,
      required: true
    },
    info_text: {
      type: String,
      required: true
    }
  },
  methods: {
    goToVideo() {
      window.open('https://www.youtube.com/watch?v=9bZkp7q19f0')
    }
  }
}
</script>

<style scoped>
.HomeProductInfo {
  display: block;
  font-family: Arial, Helvetica, sans-serif;
  justify-content: center;
  align-items: center;
  padding: 1rem;
}

.HomeProductInfoContent {
  display: flex;
  justify-content: center;
  align-items: center;
  background: transparent;
  padding: 1rem;
}

.ProductInfo-title {
  font-size: 4rem;
  color: black;
  text-align: center;
  margin-top: 5px;
  margin-bottom: 5px;
}

.ProductInfo_subtitle {
  font-size: 2.5rem;
  font-family: 'Times New Roman', Times, serif;
  font-weight: bold;
  color: var(--cyan-10);
  text-align: center;
  margin-bottom: 1rem;
}

.HomeInfoShortdescription {
  font-size: 1.8rem;
  font-family: 'Times New Roman', Times, serif;
  font-weight: bold;
  color: black;
  text-align: center;
  margin-bottom: 1rem;
}

.ProductInfo-text {
  flex: 1;
  padding: 1rem;
  padding-left: 4rem;
  font-size: 1rem;
  color: black;
  display: flex;
  flex-direction: column;
  justify-content: center;
  align-items: center;
}

.Home_button_video {
  background-color: transparent;
  color: var(--secondary-color);
  align-items: center;
  font-size: 1.2rem;
  font-weight: bold;
  border: 2px solid var(--secondary-color);
  border-radius: 20px;
  padding: 10px 10px;
  margin: 10px;
  cursor: pointer;
}

.Home_button_icon {
  width: 20px;
  height: 20px;
  margin-right: 10px;
}

.Home_button_video:hover {
  background-color: var(--secondary-color);
  color: white;
  font-size: 20px;
  font-weight: bold;
  box-shadow: 0 0 15px var(--secondary-color);
}

.Home_button_start {
  background-color: var(--primary-color);
  color: rgb(0, 0, 0);
  font-size: 1.2rem;
  font-weight: bold;
  border: 2px solid var(--primary-color);
  border-radius: 20px;
  padding: 10px 10px;
  margin: 10px;
  cursor: pointer;
}

.Home_button_start:hover {
  background-color: green;
  color: white;
  border: 2px solid green;
  box-shadow: 0 0 15px green;
}

.HomeInfo-graphic {
  flex: 1;
  display: flex;
  justify-content: center;
  align-items: center;
  margin: 20px;
  padding-bottom: 20px;
  max-height: 50%;
  max-width: 50%;
  z-index: 1;
}

.HomeInfo-graphic img {
  width: 70%;
  height: auto;
  transform: scale(1.5);
  border-radius: 20px;
  box-shadow: 0 0 15px var(--cyan-10);
  z-index: 1;
}
</style>
