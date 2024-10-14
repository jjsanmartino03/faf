<script setup lang="ts">
import Cross from './Cross-card.vue';
import InputGroup from 'primevue/inputgroup';
import Input from 'primevue/inputtext';
import Button from 'primevue/button';
import {useCrossesStore} from "../../store/crosses";
import {computed, onMounted} from "vue";

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
onMounted(async () => {
  store.getCrosses();
})
const crosses = computed(() => store.crosses)

</script>
<template>
  <main class="p-2">
    <h1 class="text-center my-2">Partidos</h1>
    <div class="flex">
      <div class="flex justify-content-center w-full">
        <InputGroup class="my-3">
          <Input placeholder="Buscar"/>
          <Button>Buscar</Button>
        </InputGroup>
      </div>
    </div>
    <div class="flex">
      <div class="flex justify-content-center" style="width: 100%;">
        <div>
          <Cross v-for="cross in crosses" :key="cross.id" :cross="cross" class="my-3"/>
        </div>
      </div>
    </div>
  </main>
</template>

<style scoped>
</style>