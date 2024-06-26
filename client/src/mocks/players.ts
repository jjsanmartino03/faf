import {mockTeams} from "./teams.ts";

const mockPlayers = [
  {
    id: 1,
    name: 'Cristiano Ronaldo',
    photo: '',
    isEnabled: true,
  },
  {
    id: 2,
    name: 'Lionel Messi',
    photo: '',
    isEnabled: true,
  },
  {
    id: 3,
    name: 'Neymar Jr',
    photo: '',
    isEnabled: false
  },
  {
    id: 4,
    name: 'Kylian Mbappé',
    photo: '',
    isEnabled: true,
  },
  {
    id: 5,
    name: 'Mohamed Salah',
    photo: '',
    isEnabled: false
  },
  {
    id: 6,
    name: 'Kevin De Bruyne',
    photo: '',
    isEnabled: false
  },
  {
    id: 7,
    name: 'Robert Lewandowski',
    photo: '',
    isEnabled: true,
  },
  {
    id: 8,
    name: 'Sadio Mané',
    photo: '',
    isEnabled: true,
  },
  {
    id: 9,
    name: 'Sergio Ramos',
    photo: '',
    isEnabled: true,
  },
  {
    id: 10,
    name: 'Virgil van Dijk',
    photo: '',
    isEnabled: true,
  },
  {
    id: 11,
    name: 'Alisson Becker',
    photo: '',
    isEnabled: true,
  },
  {
    id: 12,
    name: 'Thiago Alcântara',
    photo: '',
    isEnabled: true,
  },
  {
    id: 13,
    name: 'Joshua Kimmich',
    photo: '',
    isEnabled: true,
  },
];

mockPlayers.forEach(p => p.photo = `https://source.boringavatars.com/beam/120/${p.name}`)

export {mockPlayers}