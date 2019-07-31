import React from 'react';

export default class LyricsResult extends React.Component {
  addFavorite() {
    const {artist, song} = this.props

    this.props.addFavorite(artist, song)
  }
  render() {
    const {artist, song, lyrics} = this.props

    if (!lyrics) {
      return null
    }

    return (
      <div className="lyrics">
        <h2>{song} by {artist}</h2>
        <small>
          <a onClick={() => this.addFavorite()}>
            Add to Favorites
          </a>
        </small>
        <p>{lyrics}</p>
      </div>
    );
  }
}


