import style from './style.module.css';
import Image from 'next/image';
import Link from 'next/link';

type TPropSig = {
  signo: string;
  image: string;
  dataFim: string;
  dataInicio: string;
  link: string;
};

export default function CardSigno(props: TPropSig) {
  return (
    <div className={style.card}>
      <h3>{props.signo}</h3>
      <Image src={props.image} width="100" height="100" alt="" />
      <p>
        As pessoas que nascem entre <strong>{props.dataInicio}</strong> -{' '}
        <strong>{props.dataFim}</strong> são classificados como{' '}
        <strong>{props.signo}</strong>
      </p>
      <Link className={style.link_info} href={props.link}>
        Saiba mais
      </Link>
    </div>
  );
}
