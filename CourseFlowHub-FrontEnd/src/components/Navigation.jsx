import "../Styles/StylesNav.css";

const Navigation = () => {
  return (
    <header>
      <nav className="flex w-full justify-between items-center">
        <div className="logo">
          <img src="../src/assets/logo.png" alt="Logo plataforma" />
        </div>
        <div className="opc grid grid-flow-col grid-cols-2 w-1/2 justify-center text-center h-10 items-center">
          <div className="container-opc">
            <p>I'm student</p>
          </div>
          <div className="container-opc">
            <p className=" cursor-default">I'm professor</p>
          </div>
        </div>
      </nav>
    </header>
  );
};

export default Navigation;
