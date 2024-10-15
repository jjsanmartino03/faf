import {defineStore, Store, StoreDefinition} from "pinia";
import api from "../services/api.ts";
import {computed, ref} from "vue";

type LoginResponse = {
  token: string
}

type User = {
  name: string
  id: number
  is_staff: boolean
  team_id : number | null
}

type AuthStore = {
  token: string | null
  isAuthenticated: boolean
  user: User | null
  status: 'loading' | 'success' | 'error' | 'idle'
}

export const useAuthStore: StoreDefinition<"auth", AuthStore> = defineStore('auth', () => {
  const token = ref<string | null>(null)
  const isAuthenticated = ref<boolean>(localStorage.getItem('token') !== null)
  const user = ref<User | null>(null)
  const status = ref<'loading' | 'success' | 'error' | 'idle'>('idle')
  const isAdmin = computed(() => user.value?.is_staff || false)

  async function login(username, password) {

    try {
      this.status = 'loading'
      const response = await api.post<LoginResponse>('api-auth/', {username, password})

      this.token = response.token
      localStorage.setItem('token', response.token)
      this.isAuthenticated = true
      this.status = 'success'
      return true
    } catch (e) {
      this.status = 'error';
      console.error(e)
    }
  }

  function logout() {
    this.token = null
    this.isAuthenticated = false
    localStorage.removeItem('token')
  }

  async function getCurrentUser() {
    try {
      const response = await api.get('api/user/')
      user.value = response
      console.log(response.data, 'response');
    } catch (e) {
      return false
    }
  }

  return {
    token,
    isAuthenticated,
    user,
    status,
    login,
    logout,
    getCurrentUser,
    isAdmin
  }
})