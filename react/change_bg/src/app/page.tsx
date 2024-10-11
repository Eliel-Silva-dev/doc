import style from './page.module.css';
import { ChangeBG } from '@/components/ChangeBG';

export default function Home() {
  return (
    <main className={style.main_home}>
      <ChangeBG />
    </main>
  );
}
