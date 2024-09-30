import { Card } from '@/components/Card';
import style from './page.module.css';

export default function Home() {
  return (
    <div className={style.page}>
      <main className={style.main}>
        <Card />
        <Card />
        <Card />
      </main>
    </div>
  );
}
