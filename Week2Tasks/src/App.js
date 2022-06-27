import React from 'react';
// import ReactDOM from 'react-dom/client';
import './App.css';

// const cards = [1, 1, 2, 2, 3, 3, 4, 4, 5, 5, 6, 6, 7, 7, 8, 8, 9, 9, 10, 10, 11, 11, 12, 12];

function delay(t){
  return new Promise(resolve=> setTimeout(resolve, t));
}

function DisplayCard(props){
  let cards = [...props.cards];
  let hidden = [...props.hidden];
  let dis = [];
  for(let i = 0; i < cards.length; i++){
    if(hidden.includes(cards[i])){
      dis.push(<Card id={-1} key1={i} handleClick={props.handleClick}/>);
    }
    else{
      dis.push(<Card id={cards[i]} key1={i} handleClick = {props.handleClick}/>);
    }
  }
  return (
    dis
  );
}

class Card extends React.Component{

  handleClick(event, key){
    // console.log(event, key);
    this.props.handleClick(key);
  }

  render(){
    let curr_id = this.props.id;
    if(curr_id === -1){
      return (
        <div className="sqr" onClick={(event)=>this.handleClick(event, this.props.key1)}></div>
      );
    }
    if(curr_id > 11){
      curr_id = 23 - curr_id;
    }
    return (
      <div className="sqr" onClick={(event)=>this.handleClick(event, this.props.key1)}>{curr_id}</div>
    );
  }
}

class Game extends React.Component{

  constructor(props) {
    super(props);
    let arr = [];
    for(let i = 0; i < 24; i++){
      arr.push(i);
    }
    
    for (let i = 23; i > 1; i--) {
        var j = Math.floor(Math.random() * (i + 1));
        var temp = arr[i];
        arr[i] = arr[j];
        arr[j] = temp;
    }
    this.state = {
      cards: [...arr],
      hidden: [],
      open: [],
      completed: [],
      score: 0,
      moves: 0
    }
    this.handleClick = this.handleClick.bind(this);

    delay(2000).then(()=>{
      this.setState({hidden:[...this.state.cards]});
    });
  }

  handleClick(key){
    // console.log("Game",key);
    if(this.state.completed.includes(key)){
      return;
    }
    let temp = [...this.state.hidden];
    temp[key] = 100;
    console.log(this.state.cards);
    this.setState({hidden:temp});
    let x = [...this.state.open];
    if(x.length === 1){          //even card open.
      if(this.state.cards[x[0]] + this.state.cards[key] === 23){    //match, keep open both cards.
        this.setState({open:[]});
        let current_score = this.state.score;
        this.setState({score: current_score + 1});
        let currCom = [...this.state.completed];
        currCom.push(key);
        currCom.push(x[0]);
        this.setState({completed: currCom});
      }
      else{               //no match, close both cards.
        delay(500).then(()=>{
        let q = [...this.state.hidden];
        q[key] = this.state.cards[key];
        q[x[0]] = this.state.cards[x[0]];
        this.setState({hidden: q});
        this.setState({open: []});
        })
      }
      let current_moves = this.state.moves;
      this.setState({moves: current_moves + 1});
    }
    else{               //odd card open.
      let w = [];
      w.push(key);
      this.setState({open: w});
    }
    // console.log(this.state.score, this.state.moves);
    
  }
  
  render(){
    
    return(
    
      <div className="game">
        <div className="heading">Memory Game</div>
        <div className="scores">
            <div className="Score">Score: <div className="XScore">{this.state.score}</div></div>
            <div className="Moves">Moves: <div className="OScore">{this.state.moves}</div></div>
        </div>
        <div className="container">
          <DisplayCard cards={this.state.cards} hidden={this.state.hidden} handleClick={this.handleClick}/>
        </div>
        <button class="reset-btn" onClick={()=>{
          let arr = [];
          for(let i = 0; i < 24; i++){
            arr.push(i);
          }
          
          for (let i = 23; i > 1; i--) {
              var j = Math.floor(Math.random() * (i + 1));
              var temp = arr[i];
              arr[i] = arr[j];
              arr[j] = temp;
          }
          this.setState({
            cards: [...arr],
            hidden: [],
            open: [],
            completed: [],
            score: 0,
            moves: 0
          });
      
          delay(2000).then(()=>{
            this.setState({hidden:[...this.state.cards]});
          });
        }}>Restart Game</button>
      </div>
    );
  }
}

// const root = ReactDOM.createRoot(document.getElementById('root'));
// root.render(<Game />);

export default Game;