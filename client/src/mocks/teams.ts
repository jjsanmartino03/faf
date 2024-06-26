import Team from '../interfaces/team';

const mockTeams: Team[] = [
  {
    name: 'River Plate',
    logo: '',
    id: 1
  },
  {
    name: 'Boca Juniors',
    logo: 'a',
    id: 2
  },
  {
    name: 'Independiente',
    logo: 'a',
    id: 3
  },
  {
    name: 'Racing Club',
    logo: 'a',
    id: 4
  },
  {
    name: 'San Lorenzo',
    logo: 'a',
    id: 5
  },
  {
    name: 'Velez Sarsfield',
    logo: 'a',
    id: 6
  },
  {
    name: 'Estudiantes',
    logo: '',
    id: 7
  },
  {
    name: 'Lanus',
    logo: '',
    id: 8
  },
  {
    name: 'Rosario Central',
    logo: '',
    id: 9
  }];

mockTeams.forEach(t => t.logo = `https://source.boringavatars.com/marble/120/${t.name}`)

export {mockTeams}