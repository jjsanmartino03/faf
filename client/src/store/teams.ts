import {defineStore, StoreDefinition} from "pinia";
import api from "../services/api.ts";

export type Team = {
  name: string
  logo_url: string
}

type TeamsStore = {
  teams: Team[] | null
  isLoading: boolean
}

export const useTeamsStore: StoreDefinition<"auth", TeamsStore> = defineStore('auth', {
  state: () => ({
    teams: null,
    isLoading: false
  }),
  actions: {
    async getTeams() {
      this.isLoading = true
      try {
        this.teams = await api.get<Team[]>('api/teams')
      } catch (e) {
        alert('Error al obtener los equipos')
      } finally {
        this.isLoading = false
      }
    }
  }
});