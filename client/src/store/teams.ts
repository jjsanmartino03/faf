import {defineStore, StoreDefinition} from "pinia";
import api from "../services/api.ts";

export type Team = {
  name: string
  logo_url: string
}

type TeamCategory = {
  id: number,
  category: number
}

export type TeamWithCategories = Team & {
  categories: TeamCategory[]
}

type TeamsStore = {
  teams: Team[] | null
  team: TeamWithCategories | null
  statusGetTeams: 'loading' | 'success' | 'error' | 'idle',
  statusCreateTeam: 'loading' | 'success' | 'error' | 'idle',
  statusGetTeam: 'loading' | 'success' | 'error' | 'idle'
}

export const useTeamsStore: StoreDefinition<"teams", TeamsStore> = defineStore('teams', {
  state: () => ({
    teams: null,
    team: null,
    statusCreateTeam: 'idle',
    statusGetTeam: 'idle',
    statusGetTeams: 'idle'
  }),
  actions: {
    async getTeams() {
      try {
        this.statusGetTeams = 'loading'
        this.teams = await api.get<Team[]>('api/teams/')
        this.statusGetTeams = 'success'
      } catch (e) {
        this.statusGetTeams = 'error'
      }
    },
    async createTeam(team: Team) {
      this.statusCreateTeam = 'loading'
      try {
        await api.post('api/teams/', team)
        this.statusCreateTeam = 'success'
      } catch (e) {
        this.statusCreateTeam = 'error'
      }
    },
    async getTeam(teamId: number) {
      this.statusGetTeam = 'loading'
      try {
        const teamResult = await api.get<TeamWithCategories>(`api/teams/${teamId}/`)
        console.log(teamResult)
        this.team = teamResult
        console.log(this.team)
        this.statusGetTeam = 'success'
      } catch (e) {
        this.statusGetTeam = 'error'
        alert('Error al obtener el equipo')
      }
    }
  }
});