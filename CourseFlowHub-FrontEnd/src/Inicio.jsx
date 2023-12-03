import Navigation from "./components/Navigation";
import "./Styles/StylesContainer.css"

function Inicio() {
  return (
    <>
      <div className="container h-screen w-full flex justify-center items-center">
        <div className="container-info-neo w-3/4 h-3/4 p-10">
          <Navigation />
          <section className=" cont-ini container flex h-4/5 items-center w-full justify-around bg">
            <section className="container w-1/3 flex flex-col gap-8">
              <h1 className=" text-xl font-bold">CourseFlowHub</h1>
              <p>Flow with Online Education.</p>
              <p>
                Lorem, ipsum dolor sit amet consectetur adipisicing elit.
                Reprehenderit, quo sed et delectus laborum recusandae adipisci
                tempora dolor aspernatur optio fugit illum repudiandae ipsum,
                nesciunt, aliquam corrupti? Ducimus, ad quia!
              </p>
              <div id="container-inicio-botones">
                <a href="#" className=" btn p-2 w-28 absolute text-center">Sign up</a>
              </div>
            </section>
            <section className="container-img">
              <img
                src="https://upload.wikimedia.org/wikipedia/commons/1/1b/Square_200x200.png"
                alt=""
              />
            </section>
          </section>
        </div>
      </div>
    </>
  );
}

export default Inicio;
