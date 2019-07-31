import React from 'react';
import Favorite from './Favorite.js'

export default class Favorites extends React.Component {
  componentDidMount() {
    this.props.loadFavorites()
  }
  render() {
    const {favorites, loadLyrics} = this.props

    return (
      <div>
        <h2>Favorites</h2>
        <hr />
        <ul>
          {favorites.map(({artist, song}) =>
            <Favorite
              loadLyrics={loadLyrics}
              key={`${artist}-${song}`}
              artist={artist}
              song={song} />
          )}
        </ul>
      </div>
    );
  }
}
