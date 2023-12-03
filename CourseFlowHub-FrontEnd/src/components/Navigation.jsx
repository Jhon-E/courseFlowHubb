import "../Styles/StylesNav.css";

const Navigation = () => {
  return (
    <header>
      <nav className="flex w-full justify-between items-center">
        <div className="logo">
          <img src="../src/assets/logo.png" alt="Logo plataforma" />
        </div>
        <div className="opc flex gap-16 w-96 p-4 justify-center">
          <div className="container-opc">
            <p className=" cursor-default">I'm student</p>
            <div className="opciones">
              <p>
                <a href="#">Sign in</a>
              </p>
            </div>
          </div>
          <div className="container-opc">
            <p className=" cursor-default">I'm professor</p>
            <div className="opciones">
              <p>
                <a href="#">Sign in</a>
              </p>
            </div>
          </div>
        </div>
      </nav>
    </header>
  );
};

export default Navigation;
