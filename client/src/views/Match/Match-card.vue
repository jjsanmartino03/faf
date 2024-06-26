<script setup lang="ts">
import { defineProps, PropType, computed } from 'vue';

import Card from 'primevue/card';
import Tag from 'primevue/tag';
import Button from 'primevue/button';

const props = defineProps({
    match: {
        type: Object as PropType<MatchDto>,
        required: true
    }
});

const borderClass = computed(() => {
    switch (props.match.status) {
        case 'Approved':
            return 'border-1 border-left-3 border-primary';
        case 'Rejected':
            return 'border-1 border-left-3 border-red-700';
        case 'Verifying':
            return 'border-1 border-left-3 border-orange-300';
        case 'Available':
            return 'border-1 border-left-3 border-warning';
        default:
            return '';
    }
});

const ptBody = {
    "body": {
        "class": "pt-2 pl-2"
    }
}


interface MatchDto {
    id: number,
    date: string,
    time: string,
    category: string,
    homeTeam: string,
    awayTeam: string,
    homeBadge: string,
    awayBadge: string,
    status: string
}

</script>

<template>
    <Card :class="borderClass" :pt="ptBody">
        <template #content>
            <div class="flex justify-content-start">
                <div>
                    <Tag severity="secondary">Cat. {{ match.category }}</Tag>
                    <Tag class="mx-1" severity="secondary">{{ match.time }} hs</Tag>
                </div>
            </div>  
            <div class="flex">
                <div class="col-4">
                    <div class="text-center">
                        <img :src="match.homeBadge" alt="home team badge" class="w-4rem border-round" />
                        <p class="my-0">{{ match.homeTeam }}</p>
                    </div>
                </div>
                <div class="col-1 flex justify-content-center">
                    <div class="text-center">
                        <p>vs</p>
                    </div>
                </div>
                <div class="col-4">
                    <div class="text-center">
                        <img :src="match.awayBadge" alt="away team badge" class="w-4rem border-round" />
                        <p class="my-0">{{ match.awayTeam }}</p>
                    </div>
                </div>
                <div class="col-3 flex justify-content-center mt-3">
                    <div class="text-center">
                        <Button v-if="match.status === 'Approved'" icon="pi pi-check" raised rounded disabled
                            severity="success" class="btnSuccess" />
                        <Button v-else-if="match.status === 'Rejected'" icon="pi pi-times" raised rounded disabled
                            class="bg-red-200 border-none" />
                        <Button v-else-if="match.status === 'Verifying'" icon="pi pi-spin pi-spinner" raised rounded
                            disabled class="bg-orange-400 border-none" />
                        <Button v-else-if="match.status === 'Available'" icon="pi pi-camera" raised rounded
                            severity="contrast" />
                    </div>
                </div>
            </div>
        </template>
    </Card>
</template>

<style>

</style>