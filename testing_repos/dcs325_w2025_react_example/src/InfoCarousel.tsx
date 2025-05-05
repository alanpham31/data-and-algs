import Carousel from "react-bootstrap/Carousel";
import ExampleCarouselImage from "components/ExampleCarouselImage";

import { carouselData } from "./carouselData.js";
import "./HTMLCarousel.css";

function InfoCarousel() {
  //console.log(carouselData);
  return (
    <Carousel>
      {carouselData.map((item, index) => (
        <Carousel.Item key={index}>
          <img className="d-block w-100" src={item.image} alt={item.label} />
          <Carousel.Caption>
            <h3>{item.label}</h3>
            <p>{item.text}</p>
          </Carousel.Caption>
        </Carousel.Item>
      ))}
    </Carousel>
  );
}

export default InfoCarousel;
