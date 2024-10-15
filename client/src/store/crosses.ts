import {Team} from "./teams.ts";
import {defineStore, StoreDefinition} from "pinia";
import {ref} from "vue";
import api from "../services/api.ts";
import {useToast} from "primevue/usetoast";

export type Validation = {
  id: number
  status: string
  photo: string | null
}
export type Match = {
  id: number
  local_validation: Validation
  visitor_validation: Validation
  category: number
  cross: number
  local_team_category: number
  visitor_team_category: number
}

export type Cross = {
  id: number
  date: `${number}-${number}-${number}`
  local_team: Team
  visitor_team: Team
  matches: Match[]
}

type MatchesStore = {
  crosses: Cross[] | null
  cross: Cross | null
  statusGetCrosses: 'loading' | 'success' | 'error' | 'idle'
  statusCreateCross: 'loading' | 'success' | 'error' | 'idle'
  statusGetCross: 'loading' | 'success' | 'error' | 'idle'
}

export const useCrossesStore: StoreDefinition<"matches", MatchesStore> = defineStore('matches', () => {
    const crosses = ref<Cross[] | null>(null)
    const cross = ref<Cross | null>(null)
    const statusGetCrosses = ref<'loading' | 'success' | 'error' | 'idle'>('idle')
    const statusCreateCross = ref<'loading' | 'success' | 'error' | 'idle'>('idle')
    const statusGetCross = ref<'loading' | 'success' | 'error' | 'idle'>('idle')
    const toast = useToast();

    async function getCrosses(keyword: string) {
      try {
        statusGetCrosses.value = 'loading'
        const params: { team_name?: string } = {}
        if (keyword) {
          params.team_name = keyword
        }
        crosses.value = await api.get<Cross[]>("api/crosses/", params)

        statusGetCrosses.value = 'success'
      } catch (e) {
        statusGetCrosses.value = 'error'
        toast.add({
          severity: 'error',
          summary: 'Error',
          detail: 'Ha ocurrido un error al obtener los partidos',
          life: 3000
        });
      }
    }

    async function createCross(data: { date: string, local_team: number, visitor_team: number }) {
      statusCreateCross.value = 'loading'
      try {
        await api.post("api/crosses/", data)
        statusCreateCross.value = 'success'
        toast.add({
          severity: 'success',
          summary: 'Éxito',
          detail: 'Cruce creado correctamente',
          life: 3000
        });
      } catch (e) {
        statusCreateCross.value = 'error'
        toast.add({
          severity: 'error',
          summary: 'Error',
          detail: 'Ha ocurrido un error al crear el partido',
          life: 3000
        });
        return e
      }
    }

    console.log(statusCreateCross, 'statusCreateCross')

    return {
      crosses,
      cross,
      statusGetCrosses,
      statusCreateCross,
      statusGetCross,
      getCrosses,
      createCross,
    }
  }
)