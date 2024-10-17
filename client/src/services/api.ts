import axios, {AxiosError, AxiosHeaders, AxiosInstance, AxiosResponse} from 'axios'

class ApiClient {
  private apiClient: AxiosInstance

  constructor() {
    this.apiClient = axios.create({
      baseURL: import.meta.env.VITE_API_URL || 'http://localhost:8000/',
      withCredentials: true,
      maxRedirects: 1
    })
  }


  async get<ResponseBodyType = any, Params = any>(url, params: Params | null = null): Promise<ResponseBodyType> {
    return await this.request<ResponseBodyType>('get', url, params)
  }

  async post<ResponseBodyType = any>(url, data): Promise<ResponseBodyType> {
    return await this.request<ResponseBodyType>('post', url, data)
  }

  async put<ResponseBodyType = any>(url, data): Promise<ResponseBodyType> {
    return await this.request<ResponseBodyType>('put', url, data)
  }

  async patch<ResponseBodyType = any>(url, data): Promise<ResponseBodyType> {
    return await this.request<ResponseBodyType>('patch', url, data)
  }

  async delete<ResponseBodyType = any>(url): Promise<ResponseBodyType> {
    return await this.request<ResponseBodyType>('delete', url)
  }

  async request<ResponseBodyType = any>(method, url, data = null) {
    let headers: AxiosHeaders = new AxiosHeaders({
      'Content-Type': 'application/json'
    })
    const token = localStorage.getItem('token')
    console.log(token);
    if (token) {
      headers.set('Authorization', `Token ${token}`)
    }

    if (!url.endsWith('/')) {
      url += '/'
    }

    // await new Promise((resolve,reject) => setTimeout(resolve, 5000))

    try {
      const config = {
        method,
        url,
        data: data && method !== 'get' ? data : null,
        params: method === 'get' ? data : null,
        headers
      };
      console.log(config);
      const response = await this.apiClient.request<any, AxiosResponse<ResponseBodyType>>(config)

      return response.data
    } catch (e) {
      if (e instanceof AxiosError) {
        if (e.response?.status === 401) {
          localStorage.removeItem('token')
          window.location.href = '/login'
        }
      }
      console.log('An error has ocurred', url, method, e)
      throw e
    }
  }
}

export default new ApiClient()