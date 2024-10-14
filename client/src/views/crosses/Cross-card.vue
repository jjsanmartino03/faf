<script setup lang="ts">
import {defineProps, PropType, computed} from 'vue';

import Card from 'primevue/card';
import Tag from 'primevue/tag';
import Button from 'primevue/button';
import {Cross} from "../../store/crosses.ts";

const props = defineProps({
  cross: {
    type: Object as PropType<Cross>,
    required: true
  }
});

const borderClass = computed(() => {
  return 'border-1 border-left-3 border-primary';
  switch (props.cross) {
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
</script>

<template>
  <Card :class="borderClass" :pt="ptBody">
    <template #content>
      <div class="flex justify-content-start">
        <div>
          <Tag severity="secondary">Cat. "hola"</Tag>
          <Tag class="mx-1" severity="secondary">{{ 19 }} hs</Tag>
        </div>
      </div>
      <div class="flex">
        <div class="col-4">
          <div class="text-center">
            <img :src="cross.local_team.logo_url" alt="home team badge" class="w-4rem border-round"/>
            <p class="my-0">{{ cross.local_team.name }}</p>
          </div>
        </div>
        <div class="col-1 flex justify-content-center">
          <div class="text-center">
            <p>vs</p>
          </div>
        </div>
        <div class="col-4">
          <div class="text-center">
            <img :src="cross.visitor_team.logo_url" alt="away team badge" class="w-4rem border-round"/>
            <p class="my-0">{{ cross.visitor_team.name }}</p>
          </div>
        </div>
        <div class="col-3 flex justify-content-center mt-3">
<!--          <div class="text-center">
            <Button v-if="match.status === 'Approved'" icon="pi pi-check" raised rounded disabled
                    severity="success" class="btnSuccess"/>
            <Button v-else-if="match.status === 'Rejected'" icon="pi pi-times" raised rounded disabled
                    class="bg-red-200 border-none"/>
            <Button v-else-if="match.status === 'Verifying'" icon="pi pi-spin pi-spinner" raised rounded
                    disabled class="bg-orange-400 border-none"/>
            <Button v-else-if="match.status === 'Available'" icon="pi pi-camera" raised rounded
                    severity="contrast"/>
          </div>-->
        </div>
      </div>
    </template>
  </Card>
</template>

<style>

</style>