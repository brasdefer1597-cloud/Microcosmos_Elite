import { Project } from '../types';

export const projects: Project[] = [
  {
    id: 'oraculo-chalamandra',
    title: 'Oráculo Chalamandra',
    desc: 'Acceso prohibido en modo BIOS. Solo input, sin ornamentos.',
    url: '/oraculo',
    tag: 'Oracle AI',
    isPro: true,
    status: 'active',
    lastUpdate: '2024-12-15',
    metrics: {
      uptime: 99.8,
      performance: 245,
      users: 1247
    }
  },
  {
    id: 'ajedrez-criminal',
    title: 'Ajedrez Criminal',
    desc: 'Operación de campo: acción y veneno. Sin explicaciones técnicas.',
    url: '/ajedrez',
    tag: 'IA & Strategy',
    isPro: true,
    status: 'active',
    lastUpdate: '2024-12-14',
    metrics: {
      uptime: 99.5,
      performance: 180,
      users: 892
    }
  },
  {
    id: 'srap-realidades',
    title: 'SRAP: Realidades Crudas',
    desc: 'Telemetría cruda del Celeron y espejo de consola en tiempo real.',
    url: '/nodo-srap',
    tag: 'Semantic UI',
    isPro: true,
    status: 'beta',
    lastUpdate: '2024-12-13',
    metrics: {
      uptime: 97.2,
      performance: 320,
      users: 456
    }
  }
];
