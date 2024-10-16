<script setup lang="ts">
import Cross from './Cross-card.vue';
import InputGroup from 'primevue/inputgroup';
import Input from 'primevue/inputtext';
import Button from 'primevue/button';
import {useCrossesStore} from "../../store/crosses";
import {computed, onMounted, ref} from "vue";
import ProgressSpinner from "primevue/progressspinner";
import CreateCrossDialog from "./CreateCrossDialog.vue";
import {useAuthStore} from "../../store/auth.ts";

const matches: MatchDto[] = [
  {
    id: 1,
    date: '2021-10-10',
    time: '09:00',
    category: '2001',
    homeTeam: 'River Plate',
    awayTeam: 'Boca Juniors',
    homeBadge: 'https://source.boringavatars.com/marble/120/riverplate',
    awayBadge: 'https://source.boringavatars.com/marble/120/bocajuniors',
    status: 'Available'
  },
  {
    id: 2,
    date: '2021-10-11',
    time: '11:30',
    category: '2002',
    homeTeam: 'River Plate',
    awayTeam: 'Boca Juniors',
    homeBadge: 'https://source.boringavatars.com/marble/120/riverplate',
    awayBadge: 'https://source.boringavatars.com/marble/120/bocajuniors',
    status: 'Rejected'
  },
  {
    id: 3,
    date: '2021-10-12',
    time: '14:00',
    category: '2003',
    homeTeam: 'River Plate',
    awayTeam: 'Boca Juniors',
    homeBadge: 'https://source.boringavatars.com/marble/120/riverplate',
    awayBadge: 'https://source.boringavatars.com/marble/120/bocajuniors',
    status: 'Approved'
  },
  {
    id: 4,
    date: '2021-10-13',
    time: '16:30',
    category: '2004',
    homeTeam: 'River Plate',
    awayTeam: 'Boca Juniors',
    homeBadge: 'https://source.boringavatars.com/marble/120/riverplate',
    awayBadge: 'https://source.boringavatars.com/marble/120/bocajuniors',
    status: 'Verifying'
  },
  {
    id: 5,
    date: '2021-10-14',
    time: '17:00',
    category: '2005',
    homeTeam: 'River Plate',
    awayTeam: 'Boca Juniors',
    homeBadge: 'https://source.boringavatars.com/marble/120/riverplate',
    awayBadge: 'https://source.boringavatars.com/marble/120/bocajuniors',
    status: 'Verifying'
  }
];

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

const store = useCrossesStore();
const authStore = useAuthStore()
onMounted(async () => {
  store.getCrosses();
})
const crosses = computed(() => store.crosses)

const keyword = ref('')

const search = () => {
  store.getCrosses(keyword.value)
}

const onKeydown = (e) => {
  if (e.key === 'Enter') {
    search();
  }
};

</script>
<template>
  <h1 class="text-center my-2">Próximos Cruces</h1>
  <div class="flex flex-column gap-2">
    <div class="flex gap-2 justify-content-center w-full">
      <InputGroup>
        <Input @keydown="onKeydown" v-model="keyword" placeholder="Buscar"/>
        <Button @click="search()">Buscar</Button>
      </InputGroup>
      <Button class="h-auto" aria-label="reload" icon="pi pi-refresh" @click="store.getCrosses()"/>
    </div>
    <div v-if="authStore.isAdmin" class="w-full">
      <CreateCrossDialog :on-create-cross="search"/>
    </div>
  </div>
  <div class="flex">
    <div class="flex justify-content-center" style="width: 100%;">
      <div v-if="store.statusGetCrosses == 'loading'  " class="bg-white w-full h-full flex justify-content-center">
        <ProgressSpinner strokeWidth="4" style="width: 4rem; height: 4rem;"/>
      </div>
      <div v-if="store.statusGetCrosses == 'success'" class="w-full">
        <div v-if="crosses && crosses.length" class="w-full">
          <Cross v-for="cross in crosses" :key="cross.id" :cross="cross" class="my-3"/>
        </div>
        <div v-else>
          <div class="text-center">No se encontraron partidos</div>
        </div>
      </div>

    </div>
  </div>
</template>

<style scoped>
</style>