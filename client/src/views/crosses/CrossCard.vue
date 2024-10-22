<script setup lang="ts">
import {defineProps, PropType, computed, defineEmits} from 'vue';

import Card from 'primevue/card';
import Panel from "primevue/panel";
import Button from 'primevue/button';
import {Cross} from "../../store/crosses.ts";
import {getDateFromString} from "../../utils/dates.ts";
import {ValidationStatus} from "../../utils/constants.ts";
import {useAuthStore} from "../../store/auth.ts";
import CreateCrossDialog from "./CreateCrossDialog.vue";

const emit = defineEmits(['openDialog'])

const props = defineProps({
  cross: {
    type: Object as PropType<Cross>,
    required: true
  },
  onUpdate: {
    type: Function as PropType<() => void>,
    required: false
  }
});

const authStore = useAuthStore();

const borderClass = computed(() => {
  return 'border-1 border-left-3 border-primary';
});

console.log(authStore.user)
const isAdmin = computed(() => authStore.isAdmin);

const userTeamId = computed(() => authStore.user?.team_id ?? null);
console.log(isAdmin.value)

const getIconClassFromStatus = (status: string) => {
  switch (status) {
    case ValidationStatus.PENDING:
      return 'pi pi-camera';
    case ValidationStatus.FAILED:
      return 'pi pi-times';
    case ValidationStatus.PASSED:
      return 'pi pi-check';
    default:
      return '';
  }
}

const getSeverityFromStatus = (status: string) => {
  switch (status) {
    case ValidationStatus.PENDING:
      return 'secondary';
    case ValidationStatus.FAILED:
      return 'danger';
    case ValidationStatus.PASSED:
      return 'success';
    default:
      return '';
  }
}

const openDialog = () => {
  emit('openDialog', !isAdmin.value);
}
</script>

<template>
  <Card :class="borderClass + ' w-full'">
    <template #content>
      <div class="grid align-items-center align-content-center justify-content-center">
        <div class="col-3 flex flex-column gap-2 justify-content-end align-items-center">
          <b>{{ getDateFromString(cross.date).toLocaleDateString('es-AR') }}</b>
          <CreateCrossDialog v-if="isAdmin" :on-complete-action="() => onUpdate && onUpdate()" :edit-mode="true"
                             :cross="cross"/>
        </div>
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
      </div>

      <Panel class="mt-2" v-if="cross.matches.length" header="Partidos" toggleable :collapsed="true">
        <ul class="m-0 p-0 match-list">
          <li v-for="match in cross.matches" :key="match.id" class="match-list-item align-items-center pt-3 pb-2">
            <div class="grid align-items-center justify-content-center">
              <div :class="isAdmin ? 'col-4' : 'col-6 text-center'">{{ isAdmin ? 'Cat.' : 'Categoría' }}
                {{ match.category }}
              </div>
              <div v-if="isAdmin || userTeamId === cross.local_team.id" class="col-3 text-center">
                <Button :severity="getSeverityFromStatus(match.local_validation.status)"
                        :icon="getIconClassFromStatus(match.local_validation.status)"
                        @click="openDialog()"/>
              </div>
              <div v-if="isAdmin" class="col-2 text-center">vs</div>
              <div v-if="isAdmin || userTeamId === cross.visitor_team.id" class="col-3 text-center">
                <Button :severity="getSeverityFromStatus(match.visitor_validation.status)"
                        :icon="getIconClassFromStatus(match.visitor_validation.status)"
                        @click="openDialog()"/>
              </div>

            </div>
          </li>
        </ul>
      </Panel>
    </template>
  </Card>
</template>

<style>
.match-list {
  list-style-type: none;
}

.match-list-item {
  border-bottom: 1px solid #e0e0e0;
}

</style>