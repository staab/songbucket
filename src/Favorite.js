import React from 'react';

export default class Favorite extends React.Component {
  onClick() {
    const {artist, song} = this.props

    this.props.loadLyrics(artist, song)
  }
  render() {
    const {song, artist} = this.props

    return (
      <li onClick={() => this.onClick()}>
        <span className="favorite-song">{song}</span>
        <span className="favorite-artist">{artist}</span>
      </li>
    );
  }
}
