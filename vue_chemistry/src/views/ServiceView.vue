<template>

    <div class="service_view">
        <serviceheader/>
        <div>
            <h1> Service
            </h1>
            <div class="sorting_services">
                <!-- <ServiceCard v-for=service in services key=""/> -->
                <ServiceCard
                    v-for="service in services"
                    :key="service.servicetitle"
                    :servicetitle="service.servicetitle"
                    :servicesubtitle="service.servicesubtitle"
                    :servicedescription="service.servicedescription"
                    :serviceimage="service.serviceimage"
                    :servicelink="service.serviceLink"
                    :servicelinkvideo="service.serviceLinkVideo"
                />
            </div>

        </div>
    </div>

</template>

<script>

import serviceheader from '@/components/ServiceViewContent/ServiceHeader.vue'
import ServiceCard from '@/components/ServiceViewContent/ServiceCard.vue'

export default {
    name: "ServiceView",
    components: {
        serviceheader,
        ServiceCard
    },
    data() {
        return {
            services: [
                {
                    imageSrc: "@/assets/tutorials/Apollo4.jpeg",
                    servicetitle: "IdeeFix",
                    servicesubtitle: "Ideas and Feature Requests",
                    servicedescription: "It is a database application for submitting feature requests and ideas.",
                    serviceLink: "/Ideefix",
                },
            ]
        }
    }

}
</script>

<style scoped>

.service_view {
    display: flex;
    flex-direction: column;
    align-items: center;
    justify-content: center;
    padding: 5px;
}

.sorting_services {
    display: flex;
    flex-direction: row;
    align-items: center;
    justify-content: center;
    padding: 5px;
    width: 100%;
    height: 100%;
}

</style>