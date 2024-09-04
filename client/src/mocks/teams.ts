import Team from '../interfaces/team';

const mockTeams: Team[] = [
  {
    name: 'River Plate',
    logo_url: '',
    id: 1
  },
  {
    name: 'Boca Juniors',
    logo_url: 'a',
    id: 2
  },
  {
    name: 'Independiente',
    logo_url: 'a',
    id: 3
  },
  {
    name: 'Racing Club',
    logo_url: 'a',
    id: 4
  },
  {
    name: 'San Lorenzo',
    logo_url: 'a',
    id: 5
  },
  {
    name: 'Velez Sarsfield',
    logo_url: 'a',
    id: 6
  },
  {
    name: 'Estudiantes',
    logo_url: '',
    id: 7
  },
  {
    name: 'Lanus',
    logo_url: '',
    id: 8
  },
  {
    name: 'Rosario Central',
    logo_url: '',
    id: 9
  }];

mockTeams.forEach(t => t.logo = `https://source.boringavatars.com/marble/120/${t.name}`)

export {mockTeams}