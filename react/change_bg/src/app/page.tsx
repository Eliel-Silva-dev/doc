import style from './page.module.css';
import { Troca_bg } from './components/Troca_bg';

export default function Home() {
  return (
    <main className={style.main_home}>
      <Troca_bg />
    </main>
  );
}
