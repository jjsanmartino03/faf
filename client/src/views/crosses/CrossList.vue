<script setup lang="ts">
import Cross from './CrossCard.vue';
import InputGroup from 'primevue/inputgroup';
import Input from 'primevue/inputtext';
import Button from 'primevue/button';
import {useCrossesStore} from "../../store/crosses";
import {computed, onMounted, ref} from "vue";
import ProgressSpinner from "primevue/progressspinner";
import CreateCrossDialog from "./CreateCrossDialog.vue";
import {useAuthStore} from "../../store/auth.ts";
import CustomBreadcrumb from "../../components/CustomBreadcrumb.vue";
import UploadTeamValidationImageDialog from '../teams/UploadTeamValidationImageDialog.vue';

const store = useCrossesStore();
const authStore = useAuthStore()
onMounted(async () => {
  store.getCrosses();
  authStore.getCurrentUser()
})
const crosses = computed(() => store.crosses)

const validationId = ref<number | null>(null)

const keyword = ref('')

const search = () => {
  store.getCrosses(keyword.value)
}

const handleDialogEvent = (openDialog: boolean,validation_id: number) => {
  validationId.value = validation_id;
  showUploadTeamValidationImageDialog.value = openDialog;
}

const onKeydown = (e) => {
  if (e.key === 'Enter') {
    search();
  }
};

const home = ref({
  icon: 'pi pi-home',
  route: '/home'
})
const model = computed(() => [
  {label: 'Partidos'},
])

const showUploadTeamValidationImageDialog = ref(false);
</script>
<template>

  <header class="w-full">
  <CustomBreadcrumb class="p-0" :model="model" :home="home"/>
  <h1 class="text-center my-2">Próximos Cruces</h1>
  </header>
  <div class="flex flex-column gap-2">
    <div class="flex gap-2 justify-content-center w-full">
      <InputGroup>
        <Input @keydown="onKeydown" v-model="keyword" placeholder="Buscar"/>
        <Button @click="search()">Buscar</Button>
      </InputGroup>
      <Button class="h-auto" aria-label="reload" icon="pi pi-refresh" @click="store.getCrosses()"/>
    </div>
    <div v-if="authStore.isAdmin" class="w-full">
      <CreateCrossDialog :on-complete-action="search"/>
    </div>
  </div>
  <div class="flex">
    <div class="flex justify-content-center" style="width: 100%;">
      <div v-if="store.statusGetCrosses == 'loading'  " class="bg-white w-full h-full flex justify-content-center">
        <ProgressSpinner strokeWidth="4" style="width: 4rem; height: 4rem;"/>
      </div>
      <div v-if="store.statusGetCrosses == 'success'" class="w-full">
        <div v-if="crosses && crosses.length" class="w-full">
          <Cross :on-update="search" v-for="cross in crosses" :key="cross.id" :cross="cross" class="my-3" @openDialog="handleDialogEvent"/>
        </div>
        <div v-else>
          <div class="text-center">No se encontraron partidos</div>
        </div>
      </div>

    </div>
  </div>
  <div class="w-full">
      <UploadTeamValidationImageDialog :on-complete="search" :visible="showUploadTeamValidationImageDialog" :validationId="validationId" @update:visible="showUploadTeamValidationImageDialog = $event"/>
  </div>
</template>

<style scoped>
</style>