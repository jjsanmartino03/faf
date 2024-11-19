<script setup lang="ts">

import Breadcrumb from "primevue/breadcrumb";
import Tag from "primevue/tag";
import {PropType} from "vue";
import {computed} from "vue";

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

const isSmallScreen = computed(() => window.innerWidth <= 768)
const firstRow = computed(() => (isSmallScreen.value ? props.model.slice(0, 3) : props.model.slice(0, 4)))
const secondRow = computed(() => (isSmallScreen.value ? props.model.slice(3) : props.model.slice(4)))

</script>
<template>
    <Breadcrumb :class="className" :model="firstRow">
      <template #item="{ item, props }">
        <router-link v-if="item.route || item.label == 'Partidos'" v-slot="{ href, navigate }" :to="item.route" custom>
          <Tag :value="item.label" @click="navigate" style="cursor: pointer;" />
        </router-link>
        <span v-else>
          <span :class="[item.icon, 'text-color']" />
          <Tag severity="info">
            <span class="text-color">{{ item.label }}</span>
          </Tag>
        </span>
      </template>
    </Breadcrumb>

    <div v-if="secondRow.length" class="mt-1">
      <Breadcrumb :class="className" :model="secondRow">
        <template #item="{ item, props }">
          <router-link v-if="item.route" v-slot="{ href, navigate }" :to="item.route" custom>
            <Tag :value="item.label" @click="navigate" style="cursor: pointer;" />
          </router-link>
          <span v-else>
            <span :class="[item.icon, 'text-color']" />
            <Tag severity="info">
              <span class="text-color">{{ item.label }}</span>
            </Tag>
          </span>
        </template>
      </Breadcrumb>
    </div>
</template>