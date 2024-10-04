import styles from './page.module.css';

export default function Home() {
  return (
    <div className={styles.container}>
      <header>
        <p>Reacj JS</p>
      </header>

      <main>
        <section className={styles.section_title}>
          <h1>React js</h1>
          <p>Biblioteca javascript para criar SPAs</p>
          <a href="#">Site oficial</a>
        </section>

        <section className={styles.section_requisitos}>
          <h2>Requisitos</h2>
          <p>Veja abaixo os requisitos mínimos para se aprender react JS</p>
          <div className={styles.container_cards}>
            <div>
              <h3>HTML</h3>
              <p>Aprenda a estruturar os elementos da página com HTML</p>
            </div>
            <div>
              <h3>CSS</h3>
              <p>Aprenda a estilizar os elementos da página com CSS</p>
            </div>
            <div>
              <h3>JAVASCRIPT</h3>
              <p>Aprenda a linguagem utilizada pelo react, o JavaScript</p>
            </div>
          </div>
        </section>
      </main>

      <footer className={styles.footer}></footer>
    </div>
  );
}
