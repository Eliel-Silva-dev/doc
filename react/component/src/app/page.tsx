import { Card } from '@/components/Card';
import style from './page.module.css';

export default function Home() {
  return (
    <main className={style.secao_cards}>
      <Card />
      <Card />
      <Card />
    </main>
  );
}
