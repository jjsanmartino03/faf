<script setup lang="ts">
import {computed, defineProps, PropType, ref, toRaw} from "vue";
import Dropdown from 'primevue/dropdown';
import Button from 'primevue/button';
import Team from "../../interfaces/team.js";
import {useTeamsStore} from "../../store/teams.ts";

const props = defineProps({
  modelValue: {
    default: null,
    type: Object as PropType<Team | null>,
  },
  statusGetTeams: {
    required: true,
    type: String as PropType<string>,
  },
});

const emit = defineEmits(['update:modelValue'])

const teamsStore = useTeamsStore()

const selectedTeam = ref(props.modelValue);

const teams = computed(() => teamsStore.teams)

const updateSelectedTeam = (team: Team) => {
  selectedTeam.value = team
  emit('update:modelValue', toRaw(team))
}
</script>

<template>
  <div class="card flex justify-center w-full">

    <Dropdown filter :loading="statusGetTeams == 'loading'" v-model="selectedTeam"
              @update:model-value="updateSelectedTeam" :options="teams" optionLabel="name"
              placeholder="Elige un Equipo"
              class="w-full">
      <template #value="slotProps">
        <div v-if="slotProps.value" class="flex align-items-center">
          <img :alt="slotProps.value.id" :src="slotProps.value.logo_url"
               class="mr-2" style="width: 18px"/>
          <div>{{ slotProps.value.name }}</div>
        </div>
        <span v-else>
            {{ slotProps.placeholder }}
        </span>
      </template>
      <template #option="slotProps">
        <div class="flex align-items-center">
          <img :alt="slotProps.option.name" :src="slotProps.option.logo_url"
               :class="`mr-2`" style="width: 18px"/>
          <div>{{ slotProps.option.name }}</div>
        </div>
      </template>
    </Dropdown>
  </div>
</template>

