import {defineStore, StoreDefinition} from "pinia";
import api from "../services/api.ts";
import {useToast} from "primevue/usetoast";
import {ref} from "vue";

export type Team = {
  id: number
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

export const useTeamsStore: StoreDefinition<"teams", TeamsStore> = defineStore('teams', () => {
  const teams = ref<Team[] | null>(null);
  const team = ref<TeamWithCategories | null>(null);
  const statusGetTeams = ref<'loading' | 'success' | 'error' | 'idle'>('idle');
  const statusCreateTeam = ref<'loading' | 'success' | 'error' | 'idle'>('idle');
  const statusGetTeam = ref<'loading' | 'success' | 'error' | 'idle'>('idle');
  const toast = useToast();

  async function getTeams() {
    try {
      statusGetTeams.value = 'loading';
      teams.value = await api.get<Team[]>("api/teams/");
      statusGetTeams.value = 'success';
    } catch (e) {
      statusGetTeams.value = 'error';
    }
  }

  async function createTeam(team: Team) {
    statusCreateTeam.value = 'loading';
    try {
      await api.post("api/teams/", team);
      statusCreateTeam.value = 'success';
      toast.add({ severity: 'success', summary: 'Equipo creado', detail: 'El equipo ha sido creado correctamente', life: 3000 });
    } catch (e) {
      statusCreateTeam.value = 'error';
      toast.add({ severity: 'error', summary: 'Error', detail: 'Ha ocurrido un error al crear el equipo', life: 3000 });
    }
  }

  async function getTeam(teamId: number) {
    statusGetTeam.value = 'loading';
    try {
      const teamResult = await api.get<TeamWithCategories>(`api/teams/${teamId}/`);
      team.value = teamResult;
      statusGetTeam.value = 'success';
    } catch (e) {
      statusGetTeam.value = 'error';
    }
  }

  return {
    teams,
    team,
    statusGetTeams,
    statusCreateTeam,
    statusGetTeam,
    getTeams,
    createTeam,
    getTeam
  };
})