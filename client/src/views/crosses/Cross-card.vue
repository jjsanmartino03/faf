<script setup lang="ts">
import {defineProps, PropType, computed} from 'vue';

import Card from 'primevue/card';
import Panel from "primevue/panel";
import Button from 'primevue/button';
import {Cross} from "../../store/crosses.ts";
import {getDateFromString} from "../../utils/dates.ts";
import {ValidationStatus} from "../../utils/constants.ts";

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
</script>

<template>
  <Card :class="borderClass + ' w-full'">
    <template #content>
      <div class="grid align-items-center align-content-center justify-content-center">
        <div class="col-3">
          <b>{{ getDateFromString(cross.date).toLocaleDateString('es-AR') }}</b>
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
              <div class="col-4">Cat. {{ match.category }}</div>
              <div class="col-3 text-center">
                <Button :severity="getSeverityFromStatus(match.local_validation.status)"
                        :icon="getIconClassFromStatus(match.local_validation.status)"/>
              </div>
              <div class="col-2 text-center">vs</div>
              <div class="col-3 text-center">
                <Button :severity="getSeverityFromStatus(match.visitor_validation.status)"
                        :icon="getIconClassFromStatus(match.visitor_validation.status)"/>
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