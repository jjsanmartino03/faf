<script setup lang="ts">

import Breadcrumb from "primevue/breadcrumb";
import {PropType} from "vue";

const props = defineProps({
  model: {
    type: Array as PropType<{ label: string, route?: string, icon?: string }[]>,
    required: true
  },
  className: {
    type: String,
    default: 'py-2 px-0'
  },
  home: {
    type: Object as PropType<{ icon: string, route: string }>,
    required: false
  }
})
</script>
<template>
  <Breadcrumb :home="home" :class="className" :model="model">
    <template #item="{ item, props }">
      <router-link v-if="item.route" v-slot="{ href, navigate }" :to="item.route" custom>
        <a  :href="href" v-bind="props.action" @click="navigate">
          <span :class="[item.icon, 'text-color']"/>
          <span class="text-color">{{ item.label }}</span>
        </a>
      </router-link>
      <span v-else>
        <span :class="[item.icon, 'text-color']"/>
        <span class="text-color">{{ item.label }}</span>
      </span>
    </template>
  </Breadcrumb>
</template>