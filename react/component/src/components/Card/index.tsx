import style from './card.module.css';

export const Card = () => {
  return (
    <div className={style.container_cards}>
      <p>Componentes</p>
      <p>Facilita em manter partes menores funcionando corretamente.</p>
      <p>Você pode reutiliza-lo, ou seja, menos código para reescrever.</p>
    </div>
  );
};
