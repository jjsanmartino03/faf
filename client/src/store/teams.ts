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
const teams = ref<Team[] | null>(null);
const team = ref<TeamWithCategories | null>(null);
const statusGetTeams = ref<'loading' | 'success' | 'error' | 'idle'>('idle');
const statusCreateTeam = ref<'loading' | 'success' | 'error' | 'idle'>('idle');
const statusGetTeam = ref<'loading' | 'success' | 'error' | 'idle'>('idle');
const statusUploadImage = ref<'loading' | 'success' | 'error' | 'idle'>('idle');

export const useTeamsStore: StoreDefinition<"teams", TeamsStore> = defineStore('teams', () => {
  const toast = useToast();

  async function getTeams() {
    try {
      statusGetTeams.value = 'loading';
      teams.value = await api.get<Team[]>("api/teams/");
      statusGetTeams.value = 'success';
    } catch (e) {
      statusGetTeams.value = 'error';
      toast.add({
        severity: 'error',
        summary: 'Error',
        detail: 'Ha ocurrido un error al obtener los equipos',
        life: 3000
      });
    }
  }

  async function createTeam(team: Team) {
    statusCreateTeam.value = 'loading';
    try {
      await api.post("api/teams/", team);
      statusCreateTeam.value = 'success';
      toast.add({
        severity: 'success',
        summary: 'Equipo creado',
        detail: 'El equipo ha sido creado correctamente',
        life: 3000
      });
    } catch (e) {
      statusCreateTeam.value = 'error';
      toast.add({severity: 'error', summary: 'Error', detail: 'Ha ocurrido un error al crear el equipo', life: 3000});
      return e
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
      toast.add({
        severity: 'error',
        summary: 'Error',
        detail: 'Ha ocurrido un error al obtener el equipo',
        life: 3000
      });
    }
  }

  async function updateTeam(teamId: number, team: Team) {
    statusGetTeam.value = 'loading';
    try {
      await api.put(`api/teams/${teamId}/`, team);
      statusGetTeam.value = 'success';
      toast.add({
        severity: 'success',
        summary: 'Éxito',
        detail: 'Equipo actualizado correctamente',
        life: 3000
      });
    } catch (e) {
      statusGetTeam.value = 'error';
      toast.add({
        severity: 'error',
        summary: 'Error',
        detail: 'Ha ocurrido un error al actualizar el equipo',
        life: 3000
      });
      return e
    }
  }

  async function uploadImage(ValidationId: number, image: File) {
    try {
      statusUploadImage.value = 'loading';
      const formData = new FormData();
      formData.append('image', image);
      await api.post(`api/teams/${ValidationId}/upload_image`, formData, {
        'Content-Type': 'multipart/form-data'
      });
      statusUploadImage.value = 'success';
      toast.add({
        severity: 'success',
        summary: 'Imagen actualizada',
        detail: 'La imagen ha sido actualizada correctamente',
        life: 3000
      });
    } catch (e) {
      console.error(e)
      toast.add({
        severity: 'error',
        summary: 'Error',
        detail: 'Ha ocurrido un error al actualizar la imagen',
        life: 3000
      });
      statusUploadImage.value = 'error';
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
    getTeam,
    updateTeam,
    uploadImage,
    statusUploadImage
  };
})
